# HostGatewaySpec

Deprecated not supported since vSphere 6.5.  Settings for a gateway used to communicate with a host.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_type** | **str** | The type of the gateway used for the communication to the host.  ***Since:*** vSphere API 6.0  | 
**gateway_id** | **str** | Identifier of the gateway to be used for communction to the host.  If omitted a random gateway of this type will be selected.  ***Since:*** vSphere API 6.0  | [optional] 
**trust_verification_token** | **str** | An opaque string that the gateway may need to validate that the host it connects to is the correct host.  ***Since:*** vSphere API 6.0  | [optional] 
**host_auth_params** | [**List[KeyValue]**](KeyValue.md) | Additional opaque authentication data that the gateway may need to authenticate to the host.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_gateway_spec import HostGatewaySpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostGatewaySpec from a JSON string
host_gateway_spec_instance = HostGatewaySpec.from_json(json)
# print the JSON string representation of the object
print HostGatewaySpec.to_json()

# convert the object into a dict
host_gateway_spec_dict = host_gateway_spec_instance.to_dict()
# create an instance of HostGatewaySpec from a dict
host_gateway_spec_form_dict = host_gateway_spec.from_dict(host_gateway_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


