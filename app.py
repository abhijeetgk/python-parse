from flask import Flask,jsonify
from dataHandler import DataHandler
app = Flask(__name__)
@app.route('/')
def showdata():
     data={}
     data['pages']= dh.print_page_timestamp()
     data['csv'] = dh.print_historic_csv_data()
     return jsonify(data)
    
    # return data

dh = DataHandler()



#    print page
##
# dh.print_historic_csv_data()
# dh.print_page_timestamp();
if __name__ == '__main__':
    app.run();

