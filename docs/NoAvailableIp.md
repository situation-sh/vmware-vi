# NoAvailableIp

There are no more IP addresses available on the given network.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.no_available_ip import NoAvailableIp

# TODO update the JSON string below
json = "{}"
# create an instance of NoAvailableIp from a JSON string
no_available_ip_instance = NoAvailableIp.from_json(json)
# print the JSON string representation of the object
print NoAvailableIp.to_json()

# convert the object into a dict
no_available_ip_dict = no_available_ip_instance.to_dict()
# create an instance of NoAvailableIp from a dict
no_available_ip_form_dict = no_available_ip.from_dict(no_available_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


