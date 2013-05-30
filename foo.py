import testtrackpro

def entity_table_name(entity):
    return entity.__class__.__name__[1:]
    
def folder_defect_record_ids(ttp, folder_path):
    folder = ttp.getFolder(folder_path)
    entities = ttp.getEntityListForFolderByRecordID(folder.recordid, True)
    defectids = [e.entityrecordid for e in entities
                 if e.entitytablename == 'Defect']
    return defectids

def _public_folder_names(folders):
    return [f.name for f in folders if f.path.startswith('/Public/')]
    
def entity_folder_paths(ttp, entity):
    folders = ttp.getFolderListForEntityByRecordID(
        entity_table_name(entity), entity.recordid)
    return _public_folder_names(folders)
    
def defect_folder_paths(ttp, defect_record_id):
    folders = ttp.getFolderListForEntityByRecordID('Defect', defect_record_id)
    return _public_folder_names(folders)
    
ttp = testtrackpro.TTP('http://10.28.16.186/ttsoapcgi.wsdl',
                      'Test', 'TTP_SDK_FB_S2', 'J0V2MHv6BQ')

d = ttp.getDefect(1)
print entity_folder_paths(ttp, d)

for did in folder_defect_record_ids(ttp, 'Public/To Review'):
    d = ttp.getDefectByRecordID(did)
    print did, d.summary
    
#with ttp:
#    with ttp.editDefect(1) as d:
#        ttp.saveDefect(d)
#        pass


        
        