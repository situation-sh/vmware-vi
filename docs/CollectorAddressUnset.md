# CollectorAddressUnset

The distributed virtual switch received a reconfiguration request to activate ipfix monitoring of the switch traffic.  However, the address and/or the port of the ipfix collector has not been specified.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.collector_address_unset import CollectorAddressUnset

# TODO update the JSON string below
json = "{}"
# create an instance of CollectorAddressUnset from a JSON string
collector_address_unset_instance = CollectorAddressUnset.from_json(json)
# print the JSON string representation of the object
print CollectorAddressUnset.to_json()

# convert the object into a dict
collector_address_unset_dict = collector_address_unset_instance.to_dict()
# create an instance of CollectorAddressUnset from a dict
collector_address_unset_form_dict = collector_address_unset.from_dict(collector_address_unset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


