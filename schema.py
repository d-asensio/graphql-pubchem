from graphene import Schema, Field, ObjectType, String, NonNull, Float, Int

from .utils import get_fields
from .data_fetchers import fetch_pubchem_compound

class CompoundType(ObjectType):
    CID = NonNull(String)
    MolecularFormula = String()
    MolecularWeight = Float()
    CanonicalSMILES = String()
    IsomericSMILES = String()
    InChI = String()
    InChIKey = String()
    IUPACName = String()
    XLogP = Float()
    ExactMass = Float()
    MonoisotopicMass = Float()
    TPSA = Float()
    Complexity = Int()
    Charge = Int()
    HBondDonorCount = Int()
    HBondAcceptorCount = Int()
    RotatableBondCount = Int()
    HeavyAtomCount = Int()
    IsotopeAtomCount = Int()
    AtomStereoCount = Int()
    DefinedAtomStereoCount = Int()
    UndefinedAtomStereoCount = Int()
    BondStereoCount = Int()
    DefinedBondStereoCount = Int()
    UndefinedBondStereoCount = Int()
    CovalentUnitCount = Int()
    Volume3D = Float()
    XStericQuadrupole3D = Float()
    YStericQuadrupole3D = Float()
    ZStericQuadrupole3D = Float()
    FeatureCount3D = Int()
    FeatureAcceptorCount3D = Int()
    FeatureDonorCount3D = Int()
    FeatureAnionCount3D = Int()
    FeatureCationCount3D = Int()
    FeatureRingCount3D = Int()
    FeatureHydrophobeCount3D = Int()
    ConformerModelRMSD3D = Int()
    EffectiveRotorCount3D = Float()
    ConformerCount3D = Float()
    Fingerprint2D = String()

class Query(ObjectType):
    Compound = Field(CompoundType, CID=String())

    def resolve_Compound(self, info, CID):
        requested_fields = get_fields(info)
        compound_model_raw = fetch_pubchem_compound(CID, requested_fields.keys())
        
        return CompoundType(**compound_model_raw)

app_schema = Schema(query=Query)
