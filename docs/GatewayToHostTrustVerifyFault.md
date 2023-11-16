# GatewayToHostTrustVerifyFault

Deprecated not used since vSphere 6.5.  GatewayToHostTrustVerifyFault is thrown by the gateway used to communicate with a host, if it cannot establish a trusted connection to the host with the provided host verification token parameter.  The fault provides a list of opaque &lt;key,value&gt; properties, which the end user has to verify in order to trust the host and a verification token, which can be used to state that those exact properties are valid.  See also *HostGatewaySpec.trustVerificationToken*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_token** | **str** | A unique verification token, that can be used to state the the listed properties are valid.  ***Since:*** vSphere API 6.0  | 
**properties_to_verify** | [**List[KeyValue]**](KeyValue.md) | A key/value list of properties that need user verification in order for the gateway to trust the host to succeed.  For instance the user may need to verify an SSL thumbprint or a whole certificate.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.gateway_to_host_trust_verify_fault import GatewayToHostTrustVerifyFault

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayToHostTrustVerifyFault from a JSON string
gateway_to_host_trust_verify_fault_instance = GatewayToHostTrustVerifyFault.from_json(json)
# print the JSON string representation of the object
print GatewayToHostTrustVerifyFault.to_json()

# convert the object into a dict
gateway_to_host_trust_verify_fault_dict = gateway_to_host_trust_verify_fault_instance.to_dict()
# create an instance of GatewayToHostTrustVerifyFault from a dict
gateway_to_host_trust_verify_fault_form_dict = gateway_to_host_trust_verify_fault.from_dict(gateway_to_host_trust_verify_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


