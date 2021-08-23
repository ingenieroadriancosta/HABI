import mysql.connector
def look_for_property_db(state, building_date, city):
    if state is not None and len(state) != 0:
        state = (state+'').replace(' ', '')
    else:
        return None
    if building_date is not None and len(building_date) != 0:
        building_date = (building_date+'').replace(' ', '')
        building_date = " (a.year='%s') and " % building_date
    else:
        building_date = " "
    if city is not None and len(city) != 0:
        city = (city+'').replace(' ', '')
        city = " (a.city='%s' ) and " % (city)
    else:
        city = " "
    habidb = mysql.connector.connect(
        host="3.130.126.210",
        user="pruebas",
        password="VGbt3Day5R",
        port=3309,
        database="habi_db"
    )
    mycursor = habidb.cursor()
    mycursor.execute("select id from status where name='%s';" % state)
    status_id = mycursor.fetchall()
    if len(status_id) == 0:
        return None
    status_id = status_id[0][0]
    query = ("select "
             + "distinct "
             + "a.year as 'year', "
             + "a.id as 'pro_id', "
             + "a.address as 'address', "
             + "a.city as 'city', "
             + "(select name from status where b.status_id=a.id limit 1) as 'state', "
             + "a.price as 'price', "
             + "case "
             + "when description is null or length(description)=0 then 'SIN DESCRIPCIÓN' "
             + "else a.description "
             + "end  as 'description' "
             + " from "
             + "property a "
             + "inner join status_history b "
             + "where "
             + building_date
             + city
             + " property_id=a.id and "
             + ("(b.status_id='%s' ) " % status_id)
             + "order by year desc "
             + ";"
             )
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    habidb.close()
    res = {'datos': [{}]}
    res['datos'].pop(0)
    for x in myresult:
        val = {'year': x[0]}
        val = {
            'year': x[0],
            'pro_id': x[1],
            'address': x[2],
            'city': x[3],
            'state': x[4],
            'price': x[5]
        }
        res['datos'].append(val)
    return res

