# GatewayToHostAuthFault

Deprecated not used since vSphere 6.5.  GatewayToHostAuthFault is thrown by the gateway used to communicate with a host, if the gateway cannot authenticate to the host with the provided authentication data.  The fault provides information, which of the properties given in the authentication data are invalid or if more properties are required.  See also *HostGatewaySpec.hostAuthParams*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_properties** | **List[str]** | List of properties that have been provided in the authentication data but have wrong values.  ***Since:*** vSphere API 6.0  | 
**missing_properties** | **List[str]** | List of properties that do not have their values specified in the provided authentication data but are required.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.gateway_to_host_auth_fault import GatewayToHostAuthFault

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayToHostAuthFault from a JSON string
gateway_to_host_auth_fault_instance = GatewayToHostAuthFault.from_json(json)
# print the JSON string representation of the object
print GatewayToHostAuthFault.to_json()

# convert the object into a dict
gateway_to_host_auth_fault_dict = gateway_to_host_auth_fault_instance.to_dict()
# create an instance of GatewayToHostAuthFault from a dict
gateway_to_host_auth_fault_form_dict = gateway_to_host_auth_fault.from_dict(gateway_to_host_auth_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


