import matplotlib.pyplot as plt
import os

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

        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        plt.savefig(filename)
        plt.close()  # Close the plot to free memory