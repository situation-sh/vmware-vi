# HostFibreChannelHba

This data object type describes the Fibre Channel host bus adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_world_wide_name** | **int** | The world wide port name for the adapter.  | 
**node_world_wide_name** | **int** | The world wide node name for the adapter.  | 
**port_type** | [**FibreChannelPortTypeEnum**](FibreChannelPortTypeEnum.md) |  | 
**speed** | **int** | The current operating speed of the adapter in bits per second.  | 

## Example

```python
from vmware_vi.models.host_fibre_channel_hba import HostFibreChannelHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostFibreChannelHba from a JSON string
host_fibre_channel_hba_instance = HostFibreChannelHba.from_json(json)
# print the JSON string representation of the object
print HostFibreChannelHba.to_json()

# convert the object into a dict
host_fibre_channel_hba_dict = host_fibre_channel_hba_instance.to_dict()
# create an instance of HostFibreChannelHba from a dict
host_fibre_channel_hba_form_dict = host_fibre_channel_hba.from_dict(host_fibre_channel_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


