from requests import get

def fetch_pubchem_compound(cid, fields):
  requestable_properties = [
    'MolecularFormula',
    'MolecularWeight',
    'CanonicalSMILES',
    'IsomericSMILES',
    'InChI',
    'InChIKey',
    'IUPACName',
    'XLogP',
    'ExactMass',
    'MonoisotopicMass',
    'TPSA',
    'Complexity',
    'Charge',
    'HBondDonorCount',
    'HBondAcceptorCount',
    'RotatableBondCount',
    'HeavyAtomCount',
    'IsotopeAtomCount',
    'AtomStereoCount',
    'DefinedAtomStereoCount',
    'UndefinedAtomStereoCount',
    'BondStereoCount',
    'DefinedBondStereoCount',
    'UndefinedBondStereoCount',
    'CovalentUnitCount',
    'Volume3D',
    'XStericQuadrupole3D',
    'YStericQuadrupole3D',
    'ZStericQuadrupole3D',
    'FeatureCount3D',
    'FeatureAcceptorCount3D',
    'FeatureDonorCount3D',
    'FeatureAnionCount3D',
    'FeatureCationCount3D',
    'FeatureRingCount3D',
    'FeatureHydrophobeCount3D',
    'ConformerModelRMSD3D',
    'EffectiveRotorCount3D',
    'ConformerCount3D',
    'Fingerprint2D'
  ]

  request_properties = [prop for prop in fields if prop in requestable_properties]
  joined_properties = ','.join(request_properties)
  pubchem_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/{joined_properties}/JSON'

  pubchem_response = get(pubchem_url)
  json_data = pubchem_response.json()

  # TODO check errors in response, etc...
  return json_data['PropertyTable']['Properties'][0]