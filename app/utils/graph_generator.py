import matplotlib.pyplot as plt

class GraphGenerator:
    @staticmethod
    def generate_incident_graph(data, filename):
        services = [item['service'] for item in data]
        incidents = [item['incident_count'] for item in data]

        plt.figure(figsize=(10, 5))
        plt.bar(services, incidents, color='blue')
        plt.xlabel('Services')
        plt.ylabel('Number of Incidents')
        plt.title('Number of Incidents per Service')
        plt.savefig(filename)