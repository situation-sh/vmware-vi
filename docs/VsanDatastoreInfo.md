# VsanDatastoreInfo

Detailed information about a vSAN datastore.  ***Since:*** vSphere API 7.0.1.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_uuid** | **str** | The cluster membership identity of the datastore.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**access_gen_no** | **int** | The generation number tracking datastore accessibility.  ***Since:*** vSphere API 7.0.1.0  | [optional] 

## Example

```python
from vmware_vi.models.vsan_datastore_info import VsanDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanDatastoreInfo from a JSON string
vsan_datastore_info_instance = VsanDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print VsanDatastoreInfo.to_json()

# convert the object into a dict
vsan_datastore_info_dict = vsan_datastore_info_instance.to_dict()
# create an instance of VsanDatastoreInfo from a dict
vsan_datastore_info_form_dict = vsan_datastore_info.from_dict(vsan_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


