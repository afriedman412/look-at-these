from app import app
import os

if __name__=="__main__":
   if 'PRODUCTION' in os.environ:
      app.run()
   else:
      app.run(debug=True)