meme_dict = { "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante", 
"LOL": "Una risposta comune a qualcosa di divertente",
"ROFL": "ROFL è utilizzato come reazione a qualcosa di divertente, similea LOL"
 } 
parola = input("Scrivi una parola moderna che non capisci (usatutte le lettere maiuscole!): ") 
if parola in meme_dict.keys():
print(meme_dict[parola]) 
else:
 print("Non abbiamo ancora questa parola...Ma ci stiamo lavorando!")
