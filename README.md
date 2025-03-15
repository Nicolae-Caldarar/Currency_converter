# Currency-Convertor-Proiect-Python
Tema proiectului:
CONVERTOR DE MONEDE

Tip de proiect:
Pentru realizarea acestui proiect am creat o interfata GUI cu ajutorul modului Tkinter.

Rulare program:
Trebuie creat un environment virtual iar apoi sa fie instalate modulele “tkinter” si “requests”. 
Pentru a fi instalate se introduc urmatoarele comenzi in terminal:   pip install tkinter  pip install requests

Functionalitate:
Programul este structurat cu ajutorul a doua clase: “CurrencyConvertor” si “Interface”.
Ratele pentru conversie a monedelor sunt luate de pe acest site: https://api.exchangerate-api.com/v4/latest/USD , care este transformat in fisier JSON cu ajutorul functiei json() la linia 10: requests.get(url).json(). 

In clasa “CurrencyConvertor” este implementat algoritmul pentru conversie. In clasa “Interface” este implementat GUI-ul.
Widget-urile folosite in program sunt: meniuri dropdown, entry, label, button.
Pentru meniu-rile dropdown am folosit widget-ul Combobox. Click pe Dropdown poti alege moneda dorita.
Cu ajutorul Entry-ului in care se introduce suma convertita si a meniurilor dropdown, se obtin parametrii pentru functia ‘conversion_fct’ din clasa “Interface”.
Butonul “Convert” realizeaza conversia prin apelarea functiei ‘conversion_fct’ care la randul ei apeleaza functia ‘conversion’ din clasa “CurrencyConverter”. Acest lucru se realizeaza prin apasarea butonului. Rezultatul este introdus intru-ul Label si afisat pe ecran.

Repartizarea sarcinilor de lucru:
Nita Razvan George: Design al interfetei (culori, fonturi, aranjarea in fereastra etc.)
Caldarar Nicolae: Scheletul interfetei (adaugarea butoanelor necesare si a textelor)
Comun: Functiile de conversie

Research:
Ratele de conversie ale monedelor au fost luate din urmatorul API: https://api.exchangerate-api.com/v4/latest/USD
Pentru tkinter si requests am folosit urmatoarele site-uri:
https://www.geeksforgeeks.org/python-gui-tkinter/
https://docs.python.org/3/library/tkinter.html
https://pypi.org/project/requests/
https://www.geeksforgeeks.org/currency-converter-in-python/
