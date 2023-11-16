# MultipleCertificatesVerifyFault

MultipleCertificatesVerifyFault is thrown by the host connect method *HostSystem.ReconnectHost_Task* as well as the methods to add a host to VirtualCenter (*Folder.AddStandaloneHost_Task* and *ClusterComputeResource.AddHost_Task*) if VirtualCenter detects that the host has different SSL certificates for different management ports.  This can occur, for example, if an ESX 2.x host has different SSL certificates for the authd service (port 902) and the Management UI port (port 443). VirtualCenter is not able to manage such hosts. To fix this issue, the user should modify the host to ensure there is only one certificate for all services. Alternatively, different certificates are allowed as long as each certificate is verifiable (trusted) by the VirtualCenter server.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbprint_data** | [**List[MultipleCertificatesVerifyFaultThumbprintData]**](MultipleCertificatesVerifyFaultThumbprintData.md) | The thumbprints (and associated ports) used by the services on the host.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.multiple_certificates_verify_fault import MultipleCertificatesVerifyFault

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleCertificatesVerifyFault from a JSON string
multiple_certificates_verify_fault_instance = MultipleCertificatesVerifyFault.from_json(json)
# print the JSON string representation of the object
print MultipleCertificatesVerifyFault.to_json()

# convert the object into a dict
multiple_certificates_verify_fault_dict = multiple_certificates_verify_fault_instance.to_dict()
# create an instance of MultipleCertificatesVerifyFault from a dict
multiple_certificates_verify_fault_form_dict = multiple_certificates_verify_fault.from_dict(multiple_certificates_verify_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


