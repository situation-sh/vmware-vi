# GatewayToHostConnectFault

Deprecated not used since vSphere 6.5.  GatewayToHostConnectFault is thrown by the gateway used to communicate with a host, if an error occurs in the communication between the gateway and the host.  More details may be provided by a subfault.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Hostname of the host that the gateway is communicating with.  ***Since:*** vSphere API 6.0  | 
**port** | **int** | Port specified for the connection between the gateway and the host.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.gateway_to_host_connect_fault import GatewayToHostConnectFault

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayToHostConnectFault from a JSON string
gateway_to_host_connect_fault_instance = GatewayToHostConnectFault.from_json(json)
# print the JSON string representation of the object
print GatewayToHostConnectFault.to_json()

# convert the object into a dict
gateway_to_host_connect_fault_dict = gateway_to_host_connect_fault_instance.to_dict()
# create an instance of GatewayToHostConnectFault from a dict
gateway_to_host_connect_fault_form_dict = gateway_to_host_connect_fault.from_dict(gateway_to_host_connect_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


