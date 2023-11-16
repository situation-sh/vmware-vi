# HostTcpHba

This data object describes the Transmission Control Protocol (TCP) host bus adapter interface.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_pnic** | **str** | Device name of the associated physical NIC, if any.  Should match the *PhysicalNic.device* property of the corresponding physical NIC.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_tcp_hba import HostTcpHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostTcpHba from a JSON string
host_tcp_hba_instance = HostTcpHba.from_json(json)
# print the JSON string representation of the object
print HostTcpHba.to_json()

# convert the object into a dict
host_tcp_hba_dict = host_tcp_hba_instance.to_dict()
# create an instance of HostTcpHba from a dict
host_tcp_hba_form_dict = host_tcp_hba.from_dict(host_tcp_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


