# HostFru

Data object representing the hardware vendor identity for a given hardware component in the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Report the FRU type if available *HostFruFruType_enum*  | 
**part_name** | **str** | Part Name is used for ordering replacement.  | 
**part_number** | **str** | Part Number is used for ordering replacement.  | 
**manufacturer** | **str** | The name of the manufacturer.  | 
**serial_number** | **str** | The serial number of the part.  | [optional] 
**mfg_time_stamp** | **datetime** | The time, if any, when this FRU entry was created by manufacturer.  | [optional] 

## Example

```python
from vmware_vi.models.host_fru import HostFru

# TODO update the JSON string below
json = "{}"
# create an instance of HostFru from a JSON string
host_fru_instance = HostFru.from_json(json)
# print the JSON string representation of the object
print HostFru.to_json()

# convert the object into a dict
host_fru_dict = host_fru_instance.to_dict()
# create an instance of HostFru from a dict
host_fru_form_dict = host_fru.from_dict(host_fru_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


