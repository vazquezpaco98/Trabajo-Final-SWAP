import twint 

#Configure

c = twint.Config()
c.Username = "cuervi_"
c.Search="clo"

# Run

twint.run.Search(c)

