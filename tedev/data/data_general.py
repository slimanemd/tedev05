employee_form_data ={
    'title': 'Employe de la SEO',
    'description': 'Veuillez rensigner le formulaire avec vos informations personnelles',
    'data':  [
        { 'f':1, 'label': 'Entreprise'  , 'fields': [{'id':'id001', 'field': 'entreprise', 'placeholder': ''       }] },
        { 'f':2, 'label': 'Nom & Prénom', 'fields': [{'id':'id002', 'field': 'firstname' , 'placeholder': 'Prenom' },
                                                     {'id':'id003', 'field': 'lastname'  , 'placeholder': 'Nom'    }] },
        { 'f':1, 'label': 'Adresse'     , 'fields': [{'id':'id004', 'field': 'address'   , 'placeholder': ''       }] },
        { 'f':2, 'label': 'Ville'       , 'fields': [{'id':'id005', 'field': 'city'      , 'placeholder': 'City'   },
                                                     {'id':'id006', 'field': 'state'     , 'placeholder': 'State'  }] },
        { 'f':1, 'label': 'Email'       , 'fields': [{'id':'id007', 'field': 'email'     , 'placeholder': ''       }] },
        { 'f':1, 'label': 'Télephone'   , 'fields': [{'id':'id008', 'field': 'phone'     , 'placeholder': 'xxx-xxx-xxxx'}] }
    ]
}

participant_form_data ={
    'title': 'Inscription au Prgramme FEDEV',
    'description': 'Merci de renseigner le formulaire d inscription',
    'data':  [
        { 'f':1, 'label': 'Entreprise'  , 'fields': [{'id':'id001', 'field': 'entreprise', 'placeholder': ''       }] },
        { 'f':2, 'label': 'Nom & Prénom', 'fields': [{'id':'id002', 'field': 'firstname' , 'placeholder': 'Prenom' },
                                                     {'id':'id003', 'field': 'lastname'  , 'placeholder': 'Nom'    }] },
        { 'f':1, 'label': 'Adresse'     , 'fields': [{'id':'id004', 'field': 'address'   , 'placeholder': ''       }] },
        { 'f':2, 'label': 'Code & Ville', 'fields': [{'id':'id005', 'field': 'city'      , 'placeholder': 'City'   },
                                                     {'id':'id006', 'field': 'state'     , 'placeholder': 'State'  }] },
        { 'f':1, 'label': 'Email'       , 'fields': [{'id':'id007', 'field': 'email'     , 'placeholder': ''       }] },
        { 'f':1, 'label': 'Télephone'   , 'fields': [{'id':'id008', 'field': 'phone'     , 'placeholder': 'xxx-xxx-xxxx'}] }
    ]
}



# --------------------------------------------------------------------------------------------#
#
from tedev.core.models.model_tedevB import Entities_tedev
from tedev.data.data_tedevB import tedevB_entity_fields, tedevB_model01

mtedevB = {
        'fields' : tedevB_entity_fields,
        'model' : Entities_tedev,
        'data' :  tedevB_model01,
    }


#
model01s = { 'fyyurB' : None, 'triviaB' : None, 'tedevB' : mtedevB }


cities = [
('1', 'Brant' ),
('2', 'Bruce' ),
('3', 'Chatham et Kent ' ),
('4', 'Dufferin ' ),
('5', 'Durham' ),
('6', 'Elgin' ),
('7', 'Essex' ),
('8', 'Frontenac' ),
('9', 'Grey' ),
('10', 'Haldimand ' ),
('11', 'Haliburton ' ),
('12', 'Halton' ),
('13', 'Hamilton' ),
('14', 'Hastings' ),
('15', 'Huron' ),
('16', 'Kawartha Lakes' ),
('17', 'Lambton' ),
('18', 'Lanark' ),
('19', 'Leeds et Grenville' ),
('20', 'Lennox et Addington' ),
('21', 'Middlesex' ),
('22', 'Niagara' ),
('23', 'Norfolk' ),
('24', 'Northumberland ' ),
('25', 'Ottawa' ),
('26', 'Oxford' ),
('27', 'Peel ' ),
('28', 'Perth' ),
('29', 'Peterborough' ),
('30', 'Prescott et Russell' ),
('31', 'Prince Edward' ),
('32', 'Renfrew' ),
('33', 'Simcoe ' ),
('34', 'Stormont, Dundas et Glengarry' ),
('35', 'Toronto' ),
('36', 'Waterloo ' ),
('37', 'Wellington' ),
('38', 'York' ),
]
