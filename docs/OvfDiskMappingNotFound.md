# OvfDiskMappingNotFound


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_name** | **str** | The disk name that is not found  ***Since:*** vSphere API 4.0  | 
**vm_name** | **str** | The VM Name  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_disk_mapping_not_found import OvfDiskMappingNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDiskMappingNotFound from a JSON string
ovf_disk_mapping_not_found_instance = OvfDiskMappingNotFound.from_json(json)
# print the JSON string representation of the object
print OvfDiskMappingNotFound.to_json()

# convert the object into a dict
ovf_disk_mapping_not_found_dict = ovf_disk_mapping_not_found_instance.to_dict()
# create an instance of OvfDiskMappingNotFound from a dict
ovf_disk_mapping_not_found_form_dict = ovf_disk_mapping_not_found.from_dict(ovf_disk_mapping_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


