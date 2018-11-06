
class Printer:
    def printOutput(self, dataCollection):
            print ("Number of expanded nodes for BFS:", dataCollection[0])
            print ("Path Cost of BFS:", dataCollection[1])
            print ("Number of nodes in path: ", len(dataCollection[2]))
            print ("Path of BFS")
            for element in dataCollection[2]:
                self.printIndex(element)

            print ("")
            print ("Number of expanded nodes for A* search:", dataCollection[3])
            print ("Path Cost of A* search:", dataCollection[4])
            print ("Number of nodes in path: ", len(dataCollection[5]))
            print ("Path of A* search")
            for element in dataCollection[5]:
                self.printIndex(element)

    def printIndex(self, element):
        print('[', element.y, ', ', element.x, ']')
