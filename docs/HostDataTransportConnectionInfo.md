# HostDataTransportConnectionInfo

DataTransportConnectionInfo contains common information about data transport connections on a host.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_memory_consumed** | **int** | Static memory consumption by a connection in bytes like buffer sizes, heap sizes, etc.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.host_data_transport_connection_info import HostDataTransportConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDataTransportConnectionInfo from a JSON string
host_data_transport_connection_info_instance = HostDataTransportConnectionInfo.from_json(json)
# print the JSON string representation of the object
print HostDataTransportConnectionInfo.to_json()

# convert the object into a dict
host_data_transport_connection_info_dict = host_data_transport_connection_info_instance.to_dict()
# create an instance of HostDataTransportConnectionInfo from a dict
host_data_transport_connection_info_form_dict = host_data_transport_connection_info.from_dict(host_data_transport_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


