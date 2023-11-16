# VStorageObjectConfigInfo

Data object specifies Virtual storage object configuration  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptor_version** | **int** | The descriptor version of this object  | [optional] 
**capacity_in_mb** | **int** | The size in MB of this object.  ***Since:*** vSphere API 6.5  | 
**consumption_type** | **List[str]** | Consumption type of this object.  See also *VStorageObjectConsumptionType_enum*.  ***Since:*** vSphere API 6.5  | [optional] 
**consumer_id** | [**List[ID]**](ID.md) | IDs of the consumer objects which consume this vstorage object.  For a virtual disk, this can be VM ID(s).  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.v_storage_object_config_info import VStorageObjectConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectConfigInfo from a JSON string
v_storage_object_config_info_instance = VStorageObjectConfigInfo.from_json(json)
# print the JSON string representation of the object
print VStorageObjectConfigInfo.to_json()

# convert the object into a dict
v_storage_object_config_info_dict = v_storage_object_config_info_instance.to_dict()
# create an instance of VStorageObjectConfigInfo from a dict
v_storage_object_config_info_form_dict = v_storage_object_config_info.from_dict(v_storage_object_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


