# SingleMac

This class defines a Single MAC address.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The MAC address.  The value for this property should be in the form like \&quot;00:50:56:bc:ef:ab\&quot;.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.single_mac import SingleMac

# TODO update the JSON string below
json = "{}"
# create an instance of SingleMac from a JSON string
single_mac_instance = SingleMac.from_json(json)
# print the JSON string representation of the object
print SingleMac.to_json()

# convert the object into a dict
single_mac_dict = single_mac_instance.to_dict()
# create an instance of SingleMac from a dict
single_mac_form_dict = single_mac.from_dict(single_mac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


