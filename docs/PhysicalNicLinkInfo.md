# PhysicalNicLinkInfo

The *PhysicalNicLinkInfo* data object describes the link speed and the type of duplex communication.  The link speed indicates the bit rate in megabits per second. The duplex boolean indicates if the link is capable of full-duplex or half-duplex communication. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed_mb** | **int** | Bit rate on the link.  | 
**duplex** | **bool** | Flag to indicate whether or not the link is capable of full-duplex (\&quot;true\&quot;) or only half-duplex (\&quot;false\&quot;).  | 

## Example

```python
from vmware_vi.models.physical_nic_link_info import PhysicalNicLinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicLinkInfo from a JSON string
physical_nic_link_info_instance = PhysicalNicLinkInfo.from_json(json)
# print the JSON string representation of the object
print PhysicalNicLinkInfo.to_json()

# convert the object into a dict
physical_nic_link_info_dict = physical_nic_link_info_instance.to_dict()
# create an instance of PhysicalNicLinkInfo from a dict
physical_nic_link_info_form_dict = physical_nic_link_info.from_dict(physical_nic_link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


