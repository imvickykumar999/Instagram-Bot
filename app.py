
Render = '''
<!DOCTYPE html>
<html>
    <head>
        <title>
            GFG
        </title>
    </head>
    <body>

        <a target="_blank" 
            href="https://www.geeksforgeeks.org/live-search-using-flask-and-jquery/">
            Source Article
        </a>

        <br><br>
        <input type="text" class="live-search-box" placeholder="search here" />

        <ul class="live-search-list" type="None">
            <li>C++</li>
            <li>c</li>
            <li>Python</li>
            <li>Java</li>
            <li>Javascript</li>
            <li>Golang</li>
            <li>R</li>
            <li>Ruby</li>
            <li>Scala</li>
            <li>C#</li>
            <li>PHP</li>
            <li>Fortran</li>
            <li>Dart</li>
        </ul>

        <script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>

        <script type="text/javascript">
            jQuery(document).ready(function($){

                $('.live-search-list li').each(function(){
                    $(this).attr('data-search-term', $(this).text().toLowerCase());
                });

                $('.live-search-box').on('keyup', function(){
                    var searchTerm = $(this).val().toLowerCase();

                    $('.live-search-list li').each(function(){

                        if ($(this).filter('[data-search-term *= ' + searchTerm + ']').length > 0 || searchTerm.length < 1) {
                            $(this).show();
                        } else {
                            $(this).hide();
                        }

                    });

                });

            });
        </script>

    </body>
</html>
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return Render

if __name__ == '__main__':
   app.run(debug = True)

# python app.py
