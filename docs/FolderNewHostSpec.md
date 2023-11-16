# FolderNewHostSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_cnx_spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | 
**esx_license** | **str** | LicenseKey.  See *LicenseManager*. If supplied, new host will be updated with the license.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.folder_new_host_spec import FolderNewHostSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FolderNewHostSpec from a JSON string
folder_new_host_spec_instance = FolderNewHostSpec.from_json(json)
# print the JSON string representation of the object
print FolderNewHostSpec.to_json()

# convert the object into a dict
folder_new_host_spec_dict = folder_new_host_spec_instance.to_dict()
# create an instance of FolderNewHostSpec from a dict
folder_new_host_spec_form_dict = folder_new_host_spec.from_dict(folder_new_host_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


