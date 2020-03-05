# CS10

Feb 26/20
=========
  Created Github Repository and began planning of project

Feb 28/20
=========
  Played around with Twython Module and displaying data
  
Mar 02/20
=========
  Started work on twitter data analysis. Taking stream and determining if the data is Positive, Negitive, or Neutral

Mar 05/20
=========

  **BIG BUG FIXES FOR BIG DATA**
  What's new
  ----------
  Now writes all entrys from stream to cvs file
  ```python
      C = {   
                    'Username': [dict_data['user']['name']],
                    'Text': [dict_data['text']],
                    'Set': [sentment],
                    }           
                df = DataFrame(C, columns= ['Username', 'Text', 'Set'])
                if "RT" not in tweet:
                    export_csv = df.to_csv ('SetData.csv', index = False, header=False, mode='a')
                else:
                    pass
  ```
  

  What's fixed
  ------------
  
  Twitter puts a cap on how long I can stream data for before it gives me a KeyError. So I just made it restart the function
  ```python
      except KeyError as e: # Pass KeyError when I reach twitter stream limit and let it catch up
            print(e)
            pass
  ```
  Also because of the use of emojis if you're displaying the stream on your terminal you'll get a UnicodeTranslateError. Same thing applies here I just told it to pass
  ```python
      except UnicodeTranslateError as e:
                print(e)
                pass
  ```
