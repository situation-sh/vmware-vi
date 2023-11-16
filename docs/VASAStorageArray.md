# VASAStorageArray

Represent Storage Array  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name  ***Since:*** vSphere API 6.0  | 
**uuid** | **str** | Unique identifier  ***Since:*** vSphere API 6.0  | 
**vendor_id** | **str** | Vendor Id  ***Since:*** vSphere API 6.0  | 
**model_id** | **str** | Model Id  ***Since:*** vSphere API 6.0  | 
**discovery_svc_info** | [**List[VASAStorageArrayDiscoverySvcInfo]**](VASAStorageArrayDiscoverySvcInfo.md) | Transport information to address the array&#39;s discovery service.  | [optional] 

## Example

```python
from vmware_vi.models.vasa_storage_array import VASAStorageArray

# TODO update the JSON string below
json = "{}"
# create an instance of VASAStorageArray from a JSON string
vasa_storage_array_instance = VASAStorageArray.from_json(json)
# print the JSON string representation of the object
print VASAStorageArray.to_json()

# convert the object into a dict
vasa_storage_array_dict = vasa_storage_array_instance.to_dict()
# create an instance of VASAStorageArray from a dict
vasa_storage_array_form_dict = vasa_storage_array.from_dict(vasa_storage_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


