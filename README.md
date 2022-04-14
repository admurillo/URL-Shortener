# URL-Shortener
URL Shortener aplication developed using Django and Python 3 as a college project.
<h1 align="center">FIRST STEPS</h1>
<p>NOTE: This application was developed using Django framework, so it is necessary for its correct execution.</p>
<h3>Create database</h3>
<p>First of all, you must migrate models to store content in database using the lines below: </p>
<p align="center">>> python3 manage.py makemigrations</p>
<p align="center">>> python3 manage.py migrate</p>
<h3>Create superuser</h3>
<p>Now, database has been created but you can not add or remove content from it. You must create a superuser: </p>
<p align="center">>> python3 manage.py createsuperuser</p>
<p>Complete the required fields: </p>
<p>Username (leave blank to use 'admurillo'): example</p>
<p>Email address: example@example.com</p>
<p>Password: *****</p>
<p>Password (again): *****</p>
<p>NOTE: Password is not showed while you are writing it.</p>
<h1 align="center">RUN APPLICATION</h1>
<p>Now, you can run the program with the following line: </p>
<p align="center">>> python3 manage.py runserver {port number}</p>
<p>NOTE: If you don't specify port number, it will run at port 8000.</p>
<p>From now on, we will use port 8000.</p>
<p>Open your browser and go to <i>locahost:8000/</i>. This is the main page where stored URLs and their shortened resources will be shown. You can add a new URL using the formulary, it will generate a random resource for the specified URL.</p>
<p>If you click on one shortened resource or write it in your browser, it will redirect you to the associated URL. For example:</p>
<table align="center">
  <tr>
    <th>Shortened</th>
    <th>URL</th>
  </tr>
  <tr>
    <td>abcde</td>
    <td>https://github.com</td>
  </tr>
</table>
<p>If you go to <i>localhost:8000/abcde</i> or you click on <i>abcde</i> (table) you will be redirected to <i>https://github.com</i>.</p>
<p>To manage your content from database, go to <i>localhost:8000/admin</i>. Sign in using your username and your password. You can add content or remove stored content from it.</p>
