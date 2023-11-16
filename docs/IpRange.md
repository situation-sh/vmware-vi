# IpRange

This class specifies a range of IP addresses by using prefix.  Usage: 128.20.20.10/24. Here 128.20.20.10 is IP address and 24 is prefix length.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_prefix** | **str** | IP address prefix.  ***Since:*** vSphere API 5.5  | 
**prefix_length** | **int** | Prefix length with max value of 32 for IPv4 and 128 for IPv6.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.ip_range import IpRange

# TODO update the JSON string below
json = "{}"
# create an instance of IpRange from a JSON string
ip_range_instance = IpRange.from_json(json)
# print the JSON string representation of the object
print IpRange.to_json()

# convert the object into a dict
ip_range_dict = ip_range_instance.to_dict()
# create an instance of IpRange from a dict
ip_range_form_dict = ip_range.from_dict(ip_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


