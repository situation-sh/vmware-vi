# HostFibreChannelTargetTransport

Fibre Channel transport information about a SCSI target. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_world_wide_name** | **int** | The world wide port name of the target.  | 
**node_world_wide_name** | **int** | The world wide node name of the target.  | 

## Example

```python
from vmware_vi.models.host_fibre_channel_target_transport import HostFibreChannelTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of HostFibreChannelTargetTransport from a JSON string
host_fibre_channel_target_transport_instance = HostFibreChannelTargetTransport.from_json(json)
# print the JSON string representation of the object
print HostFibreChannelTargetTransport.to_json()

# convert the object into a dict
host_fibre_channel_target_transport_dict = host_fibre_channel_target_transport_instance.to_dict()
# create an instance of HostFibreChannelTargetTransport from a dict
host_fibre_channel_target_transport_form_dict = host_fibre_channel_target_transport.from_dict(host_fibre_channel_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


