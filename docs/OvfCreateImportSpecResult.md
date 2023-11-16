# OvfCreateImportSpecResult

The CreateImportSpecResult contains all information regarding the import that can be extracted from the OVF descriptor.  For example, this includes the list of items that the caller must upload in order to complete the import, but not the list of URLs to which the files must be uploaded. These paths are not known until the VMs have been created, ie. until *ResourcePool.importVApp* has been called.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_spec** | [**ImportSpec**](ImportSpec.md) |  | [optional] 
**file_item** | [**List[OvfFileItem]**](OvfFileItem.md) | The files that must be uploaded by the caller as part of importing the entity.  The files must be uploaded in order, because some of them may be delta files that patch already-uploaded files.  ***Since:*** vSphere API 4.0  | [optional] 
**warning** | [**List[MethodFault]**](MethodFault.md) | Non-fatal warnings from the processing.  The ImportSpec will be valid, but the user may choose to reject it based on these warnings.  ***Since:*** vSphere API 4.0  | [optional] 
**error** | [**List[MethodFault]**](MethodFault.md) | Errors that happened during processing.  Something will be wrong with the ImportSpec, or it is not present.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_create_import_spec_result import OvfCreateImportSpecResult

# TODO update the JSON string below
json = "{}"
# create an instance of OvfCreateImportSpecResult from a JSON string
ovf_create_import_spec_result_instance = OvfCreateImportSpecResult.from_json(json)
# print the JSON string representation of the object
print OvfCreateImportSpecResult.to_json()

# convert the object into a dict
ovf_create_import_spec_result_dict = ovf_create_import_spec_result_instance.to_dict()
# create an instance of OvfCreateImportSpecResult from a dict
ovf_create_import_spec_result_form_dict = ovf_create_import_spec_result.from_dict(ovf_create_import_spec_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


