# SSLVerifyFault

SSLVerifyFault is thrown by the host connect method if the VC server could not verify the authenticity of the host's SSL certificate.  Currently, we do not distinguish the various possible reasons why the certificate could not be verified because we don't provide a way for the user to overwrite these reasons other than turning off SSL certificate verification completely. The only exception is the case when the certificate was rejected because it was self-signed. This is the most likely case when the user may want to overwrite the behavior by specifying the certificate's thumbprint in the ConnectSpec the next time the user connects to the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_signed** | **bool** | Whether the host&#39;s certificate was self signed  ***Since:*** VI API 2.5  | 
**thumbprint** | **str** | The thumbprint of the host&#39;s certificate  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.ssl_verify_fault import SSLVerifyFault

# TODO update the JSON string below
json = "{}"
# create an instance of SSLVerifyFault from a JSON string
ssl_verify_fault_instance = SSLVerifyFault.from_json(json)
# print the JSON string representation of the object
print SSLVerifyFault.to_json()

# convert the object into a dict
ssl_verify_fault_dict = ssl_verify_fault_instance.to_dict()
# create an instance of SSLVerifyFault from a dict
ssl_verify_fault_form_dict = ssl_verify_fault.from_dict(ssl_verify_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


