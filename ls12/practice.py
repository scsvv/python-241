class Topology:

    def __init__(self, topologies):
        self.topologies = topologies
        self.topologies = self.__clean_topologies()

    def __clean_topologies(self):
        new_topologies = dict()
        names, ports = set(), set()
        for key, value in self.topologies.items():
            if not (key[0] in names and value[0] in names and key[1] in ports and value[1] in ports):
                
                names.add(key[0])
                names.add(value[0])
                ports.add(key[1])
                ports.add(value[1])
                
                new_topologies[key] = value
        
        return new_topologies




topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

t = Topology(topology_example)
print(t.topologies)