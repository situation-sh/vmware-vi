# HostTcpTargetTransport

Transmission Control Protocol (TCP) transport information about a target.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_tcp_target_transport import HostTcpTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of HostTcpTargetTransport from a JSON string
host_tcp_target_transport_instance = HostTcpTargetTransport.from_json(json)
# print the JSON string representation of the object
print HostTcpTargetTransport.to_json()

# convert the object into a dict
host_tcp_target_transport_dict = host_tcp_target_transport_instance.to_dict()
# create an instance of HostTcpTargetTransport from a dict
host_tcp_target_transport_form_dict = host_tcp_target_transport.from_dict(host_tcp_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


