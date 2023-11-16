# HostTcpHbaCreateSpec

A data object which specifies the parameters needed to create an NVME over TCP host bus adapter.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic** | **str** | Device name of the associated physical NIC.  Should match the *PhysicalNic.device* property of the corresponding physical NIC.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.host_tcp_hba_create_spec import HostTcpHbaCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostTcpHbaCreateSpec from a JSON string
host_tcp_hba_create_spec_instance = HostTcpHbaCreateSpec.from_json(json)
# print the JSON string representation of the object
print HostTcpHbaCreateSpec.to_json()

# convert the object into a dict
host_tcp_hba_create_spec_dict = host_tcp_hba_create_spec_instance.to_dict()
# create an instance of HostTcpHbaCreateSpec from a dict
host_tcp_hba_create_spec_form_dict = host_tcp_hba_create_spec.from_dict(host_tcp_hba_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


