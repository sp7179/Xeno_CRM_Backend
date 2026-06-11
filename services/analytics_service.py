from config.database import (
    customers_collection,
    orders_collection,
    campaigns_collection,
    communications_collection,
    campaign_analytics_collection
)


def get_overview_analytics():

    total_customers = (
        customers_collection.count_documents({})
    )

    total_orders = (
        orders_collection.count_documents({})
    )

    total_campaigns = (
        campaigns_collection.count_documents({})
    )

    total_communications = (
        communications_collection.count_documents({})
    )

    total_revenue = 0

    orders = orders_collection.find({})

    for order in orders:
        total_revenue += order.get(
            "amount",
            0
        )

    return {
        "success": True,

        "analytics": {

            "total_customers":
                total_customers,

            "total_orders":
                total_orders,

            "total_campaigns":
                total_campaigns,

            "total_communications":
                total_communications,

            "total_revenue":
                round(
                    total_revenue,
                    2
                )
        }
    }


def get_campaign_analytics():

    campaigns = list(
        campaign_analytics_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "success": True,
        "campaigns": campaigns
    }