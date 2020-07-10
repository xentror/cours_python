import requests
import bs4
import sys

class partners_graph:
    graph = {}

    def insert_partner(self, name, partner):
        partners = self.graph.get(name)

        if partners == None:
            return False
        for i in partners:
            if i == partner:
                return False

        partners.append(partner)
        return True

    def insert_new(self, name):
        partners = self.graph.get(name)

        if partners != None:
            return False

        self.graph[name] = []
        return True

    def print(self):
        print(self.graph)

    def print_to_graphviz(self):
        print("graph {")

        for key in self.graph.keys():
            for value in self.graph[key]:
                print("\t\"" + key + "\" -- \"" + value + "\"")
        print("}")

    def extract_link(self, name, partners, depth_max, curr_depth):
        links = []

        for partner in partners.find_all("a"):
            link = partner.get("href")
            if link != None and curr_depth < depth_max:
                links.append(link)
                partner_name = partner.getText()

                if partner_name != None:
                    self.insert_partner(name, partner_name)

        for link in links:
            if depth_max > curr_depth:
                self.extract_info(link, depth_max, curr_depth + 1)

    def extract_info(self, short_link, depth, curr_depth = 0):
        url = "https://tele-realite.fandom.com" + short_link
        response = requests.get(url)

        code = bs4.BeautifulSoup(response.text, 'html.parser')

        name = code.find("h2", {"data-source":"nom"})
        if name == None:
            return

        name = name.getText()
        gfs1 = code.find("div", {"data-source":"petiteamie"})
        gfs2 = code.find("div", {"data-source":"petite-amie"})

        bfs1 = code.find("div", {"data-source":"petitami"})
        bfs2 = code.find("div", {"data-source":"petit-ami"})

        if not self.insert_new(name):
            return

        error = True
        if gfs1 != None:
            self.extract_link(name, gfs1, depth, curr_depth)
        if gfs2 != None:
            self.extract_link(name, gfs2, depth, curr_depth)
        if bfs1 != None:
            self.extract_link(name, bfs1, depth, curr_depth)
        if bfs2 != None:
            self.extract_link(name, bfs2, depth, curr_depth)

name = sys.argv[1]
depth = int(sys.argv[2])

g = partners_graph()
g.extract_info("/fr/wiki/" + name, depth)
g.print_to_graphviz()
