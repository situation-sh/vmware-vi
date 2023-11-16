# MacRange

This class defines a range of MAC address.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | MAC address.  ***Since:*** vSphere API 5.5  | 
**mask** | **str** | Mask that is used in matching the MAC address.  A MAC address is considered matched if the \&quot;and\&quot; operation of the mask on the MAC address and *MacRange.address* yields the same result. For example, a MAC of \&quot;00:A0:FF:14:FF:29\&quot; is considered matched for a *MacRange.address* of \&quot;00:A0:C9:14:C8:29\&quot; and a *MacRange.mask* of \&quot;FF:FF:00:FF:00:FF\&quot;.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.mac_range import MacRange

# TODO update the JSON string below
json = "{}"
# create an instance of MacRange from a JSON string
mac_range_instance = MacRange.from_json(json)
# print the JSON string representation of the object
print MacRange.to_json()

# convert the object into a dict
mac_range_dict = mac_range_instance.to_dict()
# create an instance of MacRange from a dict
mac_range_form_dict = mac_range.from_dict(mac_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


