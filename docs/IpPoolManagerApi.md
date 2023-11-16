# vmware_vi.IpPoolManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_pool_manager_allocate_ipv4_address**](IpPoolManagerApi.md#ip_pool_manager_allocate_ipv4_address) | **POST** /IpPoolManager/{moId}/AllocateIpv4Address | Allocates an IPv4 address from an IP pool. 
[**ip_pool_manager_allocate_ipv6_address**](IpPoolManagerApi.md#ip_pool_manager_allocate_ipv6_address) | **POST** /IpPoolManager/{moId}/AllocateIpv6Address | Allocates an IPv6 address from an IP pool. 
[**ip_pool_manager_create_ip_pool**](IpPoolManagerApi.md#ip_pool_manager_create_ip_pool) | **POST** /IpPoolManager/{moId}/CreateIpPool | Create a new IP pool. 
[**ip_pool_manager_destroy_ip_pool**](IpPoolManagerApi.md#ip_pool_manager_destroy_ip_pool) | **POST** /IpPoolManager/{moId}/DestroyIpPool | Destroys an IP pool on the given datacenter. 
[**ip_pool_manager_query_ip_allocations**](IpPoolManagerApi.md#ip_pool_manager_query_ip_allocations) | **POST** /IpPoolManager/{moId}/QueryIPAllocations | Query IP allocations by IP pool and extension key. 
[**ip_pool_manager_query_ip_pools**](IpPoolManagerApi.md#ip_pool_manager_query_ip_pools) | **POST** /IpPoolManager/{moId}/QueryIpPools | Return the list of IP pools for a datacenter. 
[**ip_pool_manager_release_ip_allocation**](IpPoolManagerApi.md#ip_pool_manager_release_ip_allocation) | **POST** /IpPoolManager/{moId}/ReleaseIpAllocation | Releases an IP allocation back to it&#39;s IP pool. 
[**ip_pool_manager_update_ip_pool**](IpPoolManagerApi.md#ip_pool_manager_update_ip_pool) | **POST** /IpPoolManager/{moId}/UpdateIpPool | Update an IP pool on a datacenter. 


# **ip_pool_manager_allocate_ipv4_address**
> str ip_pool_manager_allocate_ipv4_address(mo_id, allocate_ipv4_address_request_type)

Allocates an IPv4 address from an IP pool. 

Allocates an IPv4 address from an IP pool.  Allocated IP addresses are reserved in the IP pool until released by calling *IpPoolManager.ReleaseIpAllocation*, or until the IP pool is configured to have an IP range that does not contain the IP address, or until the IP pool is destroyed.  The caller must be a vCenter extension. Refer to *ExtensionManager* for details on vCenter extensions.  The caller specifies a per extension unique allocation ID. Calling this function twice with the same allocation ID for the same pool yields the same IP address. This makes it possible to do idempotent allocations.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.allocate_ipv4_address_request_type import AllocateIpv4AddressRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    allocate_ipv4_address_request_type = vmware_vi.AllocateIpv4AddressRequestType() # AllocateIpv4AddressRequestType | 

    try:
        # Allocates an IPv4 address from an IP pool. 
        api_response = api_instance.ip_pool_manager_allocate_ipv4_address(mo_id, allocate_ipv4_address_request_type)
        print("The response of IpPoolManagerApi->ip_pool_manager_allocate_ipv4_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_allocate_ipv4_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **allocate_ipv4_address_request_type** | [**AllocateIpv4AddressRequestType**](AllocateIpv4AddressRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An IPv4 address if the pool has an available IPv4 address in its address ranges, otherwise the empty string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_allocate_ipv6_address**
> str ip_pool_manager_allocate_ipv6_address(mo_id, allocate_ipv6_address_request_type)

Allocates an IPv6 address from an IP pool. 

Allocates an IPv6 address from an IP pool.  Allocated IP addresses are reserved in the IP pool until released by calling *IpPoolManager.ReleaseIpAllocation*, or until the IP pool is configured to have an IP range that does not contain the IP address, or until the IP pool is destroyed.  The caller must be a vCenter extension. Refer to *ExtensionManager* for details on vCenter extensions.  The caller specifies a per extension unique allocation ID. Calling this function twice with the same allocation ID for the same pool yields the same IP address. This makes it possible to do idempotent allocations.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.allocate_ipv6_address_request_type import AllocateIpv6AddressRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    allocate_ipv6_address_request_type = vmware_vi.AllocateIpv6AddressRequestType() # AllocateIpv6AddressRequestType | 

    try:
        # Allocates an IPv6 address from an IP pool. 
        api_response = api_instance.ip_pool_manager_allocate_ipv6_address(mo_id, allocate_ipv6_address_request_type)
        print("The response of IpPoolManagerApi->ip_pool_manager_allocate_ipv6_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_allocate_ipv6_address: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **allocate_ipv6_address_request_type** | [**AllocateIpv6AddressRequestType**](AllocateIpv6AddressRequestType.md)|  | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An IPv6 address if the pool has an available IPv6 address in its address ranges, otherwise the empty string.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_create_ip_pool**
> int ip_pool_manager_create_ip_pool(mo_id, create_ip_pool_request_type)

Create a new IP pool. 

Create a new IP pool.  The name field must be defined, all other fields are optional. If unset, they will be given default values.  The ID for the pool is generated by the server and should not be defined on the pool object passed to this method.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_ip_pool_request_type import CreateIpPoolRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_ip_pool_request_type = vmware_vi.CreateIpPoolRequestType() # CreateIpPoolRequestType | 

    try:
        # Create a new IP pool. 
        api_response = api_instance.ip_pool_manager_create_ip_pool(mo_id, create_ip_pool_request_type)
        print("The response of IpPoolManagerApi->ip_pool_manager_create_ip_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_create_ip_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_ip_pool_request_type** | [**CreateIpPoolRequestType**](CreateIpPoolRequestType.md)|  | 

### Return type

**int**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The generated ID for the pool  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_destroy_ip_pool**
> ip_pool_manager_destroy_ip_pool(mo_id, destroy_ip_pool_request_type)

Destroys an IP pool on the given datacenter. 

Destroys an IP pool on the given datacenter.  Looks up the pool on the datacenter by ID and deletes it. If the pool is in use, the method throws InvalidState unless the force flag is true.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.destroy_ip_pool_request_type import DestroyIpPoolRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    destroy_ip_pool_request_type = vmware_vi.DestroyIpPoolRequestType() # DestroyIpPoolRequestType | 

    try:
        # Destroys an IP pool on the given datacenter. 
        api_instance.ip_pool_manager_destroy_ip_pool(mo_id, destroy_ip_pool_request_type)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_destroy_ip_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **destroy_ip_pool_request_type** | [**DestroyIpPoolRequestType**](DestroyIpPoolRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidState***: if the pool is in use and the force flag is false  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_query_ip_allocations**
> List[IpPoolManagerIpAllocation] ip_pool_manager_query_ip_allocations(mo_id, query_ip_allocations_request_type)

Query IP allocations by IP pool and extension key. 

Query IP allocations by IP pool and extension key.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.ip_pool_manager_ip_allocation import IpPoolManagerIpAllocation
from vmware_vi.models.query_ip_allocations_request_type import QueryIPAllocationsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_ip_allocations_request_type = vmware_vi.QueryIPAllocationsRequestType() # QueryIPAllocationsRequestType | 

    try:
        # Query IP allocations by IP pool and extension key. 
        api_response = api_instance.ip_pool_manager_query_ip_allocations(mo_id, query_ip_allocations_request_type)
        print("The response of IpPoolManagerApi->ip_pool_manager_query_ip_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_query_ip_allocations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_ip_allocations_request_type** | [**QueryIPAllocationsRequestType**](QueryIPAllocationsRequestType.md)|  | 

### Return type

[**List[IpPoolManagerIpAllocation]**](IpPoolManagerIpAllocation.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting list of @{link IpAllocation}.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_query_ip_pools**
> List[IpPool] ip_pool_manager_query_ip_pools(mo_id, query_ip_pools_request_type)

Return the list of IP pools for a datacenter. 

Return the list of IP pools for a datacenter.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.ip_pool import IpPool
from vmware_vi.models.query_ip_pools_request_type import QueryIpPoolsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_ip_pools_request_type = vmware_vi.QueryIpPoolsRequestType() # QueryIpPoolsRequestType | 

    try:
        # Return the list of IP pools for a datacenter. 
        api_response = api_instance.ip_pool_manager_query_ip_pools(mo_id, query_ip_pools_request_type)
        print("The response of IpPoolManagerApi->ip_pool_manager_query_ip_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_query_ip_pools: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_ip_pools_request_type** | [**QueryIpPoolsRequestType**](QueryIpPoolsRequestType.md)|  | 

### Return type

[**List[IpPool]**](IpPool.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resulting list of pools.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_release_ip_allocation**
> ip_pool_manager_release_ip_allocation(mo_id, release_ip_allocation_request_type)

Releases an IP allocation back to it's IP pool. 

Releases an IP allocation back to it's IP pool.  Attempting to release an IP allocation that is not allocated from the specified IP pool with the specified allocation ID silently fails. This makes it possible to release IP allocations idempotently.  All IP addresses allocated by an extension are automatically released if the extension is unregistered from vCenter.  ***Since:*** vSphere API 5.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.release_ip_allocation_request_type import ReleaseIpAllocationRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    release_ip_allocation_request_type = vmware_vi.ReleaseIpAllocationRequestType() # ReleaseIpAllocationRequestType | 

    try:
        # Releases an IP allocation back to it's IP pool. 
        api_instance.ip_pool_manager_release_ip_allocation(mo_id, release_ip_allocation_request_type)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_release_ip_allocation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **release_ip_allocation_request_type** | [**ReleaseIpAllocationRequestType**](ReleaseIpAllocationRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_manager_update_ip_pool**
> ip_pool_manager_update_ip_pool(mo_id, update_ip_pool_request_type)

Update an IP pool on a datacenter. 

Update an IP pool on a datacenter.  The pool to update is looked up from the value of the id field.  All fields in the pool except the id are optional. Only defined values are stored on the server.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_ip_pool_request_type import UpdateIpPoolRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.IpPoolManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_ip_pool_request_type = vmware_vi.UpdateIpPoolRequestType() # UpdateIpPoolRequestType | 

    try:
        # Update an IP pool on a datacenter. 
        api_instance.ip_pool_manager_update_ip_pool(mo_id, update_ip_pool_request_type)
    except Exception as e:
        print("Exception when calling IpPoolManagerApi->ip_pool_manager_update_ip_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_ip_pool_request_type** | [**UpdateIpPoolRequestType**](UpdateIpPoolRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

