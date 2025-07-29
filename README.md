markdown
# Target1 MCP Server

## Overview

Target1 is a powerful Multi-Channel Platform (MCP) server designed to enhance your retail and product management capabilities. With its comprehensive set of tools, Target1 allows users to efficiently query and manage stores, categories, products, and reviews, similar to what you would find on official retail websites.

## Features

- **Popularity**: 9.8
- **Service Level**: 100%
- **Latency**: 1000ms

## Subscription Plans

Target1 offers flexible subscription plans to cater to various needs:

- **BASIC**: Free
- **PRO**: $10.00 / month
- **ULTRA**: $30.00 / month
- **MEGA**: $300.00 / month

## Tools and Functionalities

Target1 MCP server provides a wide array of tools to facilitate various operations:

### Auto-Complete
- **auto-complete**: Get suggestions by inputting a term or phrase.

### Category Management
- **categories/v2/list**: List all root and subcategories.
- **categories/list (Deprecated)**: Legacy function for listing categories.

### Product Management
- **products/search-by-barcode**: Search for products using a barcode.
- **products/v2/list**: List products in a specific store with various options and filters.
- **products/v3/get-details**: Retrieve detailed information about a product.
- **products/v2/list-recommended**: Discover more products to consider.
- **products/list-recommended (Deprecated)**: Legacy function for recommended products.
- **products/list (Deprecated)**: Legacy function for listing products in a store.
- **products/list-collection (Deprecated)**: Legacy function for listing collections related to a product.
- **products/get-details (Deprecated)**: Legacy function for getting product details.
- **products/v2/get-details (Deprecated)**: Legacy function for getting product details.

### Review Management
- **reviews/v2/list**: List reviews associated with a product.
- **reviews/list (Deprecated)**: Legacy function for listing product reviews.

## Tool Declarations

Each tool comes with specific parameters to tailor your queries and actions:

- **auto_complete**: Suggests products based on a term or phrase.
- **v2_list**: Lists categories, with options for child category exploration.
- **products_search_by_barcode**: Requires store ID and barcode for product search.
- **v3_get_details**: Needs product and store IDs for detailed product information.
- **v2_list_recommended**: Lists additional product recommendations.
- **products_list**: Includes parameters for store location, pagination, sorting, and search filtering.
- **products_list_collection**: Lists entire collections related to specified products.
- **reviews_list**: Lists product reviews with sorting and pagination options.

## Conclusion

Target1 MCP server is a versatile and robust platform, ideal for enhancing your retail data management and customer experience. Whether you're managing product catalogs or exploring new product suggestions, Target1 provides the tools necessary to optimize your operations efficiently.

For more information on subscription plans and detailed tool usage, please explore the available options within the server.