import json
from flask import jsonify
from flask import Flask,request
app = Flask(__name__)
@app.route("/", methods=['POST'])
def home():
  with open('self_contact.json') as json_file:
      data = json.load(json_file)
  # for info in data:
  #     if info['firstName'] == 'John':
  #         print(info['phone'])
  print('here')
  # print(request.data.rstrip())
  get_data = request.data
  final_data = json.loads(get_data)
  print(final_data)
  endpnt = final_data["queryResult"]["action"]
  print(endpnt)
  if(endpnt == 'payments'):
      amount = final_data["queryResult"]["parameters"]["unit-currency"]["amount"]
      currency = final_data["queryResult"]["parameters"]["unit-currency"]["currency"]
      name = final_data["queryResult"]["parameters"]["person"]["name"]
      action = final_data["queryResult"]["parameters"]["payment_type"]
      print(amount)
      print(currency)
      print(name)
      print(action)
      message = ''
      message2 = ''
      for info in data:
          if action.lower() == "send":
              if info['firstName'] == name.lower():
                  info["balanceAvailable"] = info["balanceAvailable"] + amount
                  message = str(amount)+"$ transferred to "+name
              elif info['firstName'] == 'self':
                  info["balanceAvailable"] = info["balanceAvailable"] - amount
                  if amount > info["maxtransferred"] + 200:
                      message = "This is embarrassing but an Anomaly is Detected in your account"
                      message2 = "Please enter the last 4 digit of your account number"
                      break
          elif action.lower() == "request" :
              message = str(amount)+"$ requested from "+name
      for info in data:
          if info['firstName'] == 'self' and info['lock']==1:
              message = "My bad! Unfortunatley your account is locked, we can't process your transaction"
      print(message)
      reply = {
          "fulfillmentText": str(message)+"\n\n"+str(message2)
          # { "fulfillmentText": str(message2) }
      }
      return reply
  elif endpnt == 'payments.anomaly':
      print("inside")
      message = ''
      get_data = request.data
      final_data = json.loads(get_data)
      last4 = final_data["queryResult"]["parameters"]["number"]
      amount = final_data['queryResult']['outputContexts'][1]['parameters']['unit-currency']['amount']
      name = final_data['queryResult']['outputContexts'][1]['parameters']['person']['name']
      print(last4)
      for info in data:
          if info['firstName'] == 'self':
              acc_no = info['accountNumber']
      if last4 == int(acc_no[-4:]):
          message = "You are good to go with this transaction. $"+str(amount)+"transferred to "+str(name)
      else:
          message = "Oh snap! Your number doesn't match. We have blocked your account, Please contact your nearest branch"
          with open("self_contact.json", "r") as jsonFile:
              data = json.load(jsonFile)
              for info in data:
                  if info['firstName'] == 'self':
                      info['lock'] = 1
          with open("self_contact.json", "w") as jsonFile:
              json.dump(data, jsonFile)
      reply = {
          "fulfillmentText": str(message)
          # { "fulfillmentText": str(message2) }
      }
      return reply
if __name__ == "__main__":
  app.run(debug=True,port = 80)