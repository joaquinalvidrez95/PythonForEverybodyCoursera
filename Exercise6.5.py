text = "X-DSPAM-Confidence:    0.8475"
print("{}".format(float(text[text.find('0'):])))
