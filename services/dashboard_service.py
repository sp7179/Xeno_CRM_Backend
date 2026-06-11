from config.database import (
    customers_collection,
    orders_collection,
    campaigns_collection,
    communications_collection
)


def get_dashboard_overview():

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

    orders = list(
        orders_collection.find({})
    )

    for order in orders:

        total_revenue += order.get(
            "amount",
            0
        )

    revenue_chart = [
        {
            "month": "Jan",
            "revenue": 0
        },
        {
            "month": "Feb",
            "revenue": 0
        },
        {
            "month": "Mar",
            "revenue": 0
        },
        {
            "month": "Apr",
            "revenue": 0
        },
        {
            "month": "May",
            "revenue": 0
        },
        {
            "month": "Jun",
            "revenue": 0
        },
        {
            "month": "Jul",
            "revenue": 0
        },
        {
            "month": "Aug",
            "revenue": 0
        },
        {
            "month": "Sep",
            "revenue": 0
        },
        {
            "month": "Oct",
            "revenue": 0
        },
        {
            "month": "Nov",
            "revenue": 0
        },
        {
            "month": "Dec",
            "revenue": 0
        }
    ]

    for order in orders:

        if "order_date" in order:

            month_index = (
                order["order_date"].month
                - 1
            )

            revenue_chart[
                month_index
            ]["revenue"] += (
                order.get(
                    "amount",
                    0
                )
            )

    recent_campaigns = list(
        campaigns_collection.find(
            {},
            {
                "_id": 0
            }
        )
        .sort(
            "created_at",
            -1
        )
        .limit(5)
    )

    return {
        "success": True,

        "dashboard": {

            "overview": {

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
            },

            "revenue_chart":
                revenue_chart,

            "recent_campaigns":
                recent_campaigns
        }
    }