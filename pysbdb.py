import numpy as np
import json
import requests

#collection of utility routines to query the NASA JPL hosted Small Body Database for orbit and covariances of minor planets

class fetch_data:
  
  def get_all(tname):
    """Fetch all data of a minor planet at a given epoch from the NASA JPL web API

        Python dependencies: json, requests

        Input: string, object name or designation (e.g. 'Eros')
        Output: dictionary containing orbital and physical properties of the target

        For details see:
        https://ssd-api.jpl.nasa.gov/doc/sbdb.html
    """
    url="https://ssd-api.jpl.nasa.gov/sbdb.api?sstr="+tname+"&cov=mat&phys-par=true&full-prec=true"

    r=requests.request("GET",url)
    ast=json.loads(r.text)
    return ast


  def cometary_elements(tname):
        """Acquire cometary orbital elements of a minor planet at a given epoch from the NASA JPL web API

        Dependencies: json, requests

        Input: string, object name or designation (e.g. 'Eros')
        Output: [epoch (JD), cometary elements [e,q(au),tp(JD),node(deg),peri(deg),inc(deg)]]

        For details see:
        https://ssd-api.jpl.nasa.gov/doc/sbdb.html

        """

        url="https://ssd-api.jpl.nasa.gov/sbdb.api?sstr="+tname+"&cov=mat&phys-par=true&full-prec=true"

        r=requests.request("GET",url)
        ast=json.loads(r.text)

        #absolute magnitude H
        h_v=ast['phys_par'][0]['value']

        #epoch of orbital elements at Tref [JD]
        epoch_jd=float(ast['orbit']['epoch'])

        #orbital elements
        elem=ast['orbit']['elements']

        hdr=[]
        val=[]
        for i in range(len(elem)):
            hdr.append(elem[i]['name'])
            val.append(elem[i]['value'])

        #pic cometary orbital elements: e,q[au],tp[MJD],node[deg],peri[deg],inc[deg]
        idx=[0,2,7,4,5,3]
        elements=[]
        for i in idx:
            if(elem[i]['name']=='tp'):
                elements.append(float(elem[i]['value']))
            else:
                elements.append(float(elem[i]['value']))

        return [epoch_jd,elements]

  def cometary_ele_cov(tname):
        """Acquire cometary orbital elements and the corresponding covariance matrix of a minor planet at a given epoch from NASA JPL's web API

        Dependencies: json, requests
        Input: string, object name or designation (e.g. 'Eros')
        Output: [epoch (JD), cometary elements [e,q(au),tp(JD),node(deg),peri(deg),inc(deg)],[6x6 or 9x9 covariance matrix]]

        For details see:
        https://ssd-api.jpl.nasa.gov/doc/sbdb.html

        """

        url="https://ssd-api.jpl.nasa.gov/sbdb.api?sstr="+tname+"&cov=mat&phys-par=true&full-prec=true"

        r=requests.request("GET",url)
        ast=json.loads(r.text)

        #absolute magnitude H
        h_v=ast['phys_par'][0]['value']

        #epoch of orbital elements at Tref [JD]
        epoch_jd=float(ast['orbit']['covariance']['epoch'])

        elem=ast['orbit']['covariance']['elements']
        hdr=[]
        val=[]
        for i in range(len(elem)):
            hdr.append(elem[i]['name'])
            val.append(float(elem[i]['value']))
        elements=val

        #square root covariance matrix for cometary orbital elements
        mat=(np.array(ast['orbit']['covariance']['data'])).astype(float)
        #print(mat)
        return [epoch_jd,elements,mat]

  def kepler_elements(tname):
        """Acquire Keplerian orbital elements of a minor planet at a given epoch from NASA JPL's web API

        Dependencies: json, requests
        Input: string, object name or designation (e.g. 'Eros')
        Output: [epoch (JD), cometary elements [a(au),e,i(deg),peri(deg),node(deg),M(deg)]]

        For details see:
        https://ssd-api.jpl.nasa.gov/doc/sbdb.html

        """

        url="https://ssd-api.jpl.nasa.gov/sbdb.api?sstr="+tname+"&cov=mat&phys-par=true&full-prec=true"

        r=requests.request("GET",url)
        ast=json.loads(r.text)

        #absolute magnitude H
        h_v=ast['phys_par'][0]['value']

        #epoch of orbital elements at Tref [JD]
        epoch_jd=float(ast['orbit']['epoch'])

        #orbital elements ['e', 'a', 'q', 'i', 'om', 'w', 'ma', 'tp', 'per', 'n', 'ad']
        elem=ast['orbit']['elements']

        hdr=[]
        val=[]
        for i in range(len(elem)):
            hdr.append(elem[i]['name'])
            val.append(elem[i]['value'])

        #pic cometary orbital elements: e,q[au],tp[MJD],node[deg],peri[deg],inc[deg]
        idx=[1,0,3,5,4,6]
        elements=[]
        for i in idx:
            if(elem[i]['name']=='tp'):
                elements.append(float(elem[i]['value']))
            else:
                elements.append(float(elem[i]['value']))

        return [epoch_jd,elements]
