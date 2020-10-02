from twilio.rest import Client

account_sid = 'ACcbebc32533f0dd339de1f3f15321993e'
auth_token = 'e37e34f9899446b4abffdb8355095ba1'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+16094546556',
    body='Hello Sire :-)',
    to='+33689346976'
)

print(message.sid)