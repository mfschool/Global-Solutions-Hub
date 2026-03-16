# MGPS Reliability Tools
# Developed by: Syed Hilaluddin Madany

def oxygen_reserve_hours(tank_liters, level_pct, flow_lpm):
    """Calculates hours of oxygen left in a VIE tank.
    
    Assumes 860 as a conversion factor for compressed gas volume.
    Inputs: tank_liters (float), level_pct (0-100), flow_lpm (float > 0).
    """
    if not (0 <= level_pct <= 100) or flow_lpm <= 0 or tank_liters <= 0:
        raise ValueError("Invalid inputs: level_pct must be 0-100, flow_lpm and tank_liters must be positive.")
    # Calculate expanded gas volume in liters (constant 860 is domain-specific)
    total_liters_gas = tank_liters * (level_pct / 100) * 860
    hours_left = total_liters_gas / (flow_lpm * 60)
    return round(hours_left, 1)

def dew_point_alert(temp):
    """Safety check for Medical Air quality."""
    if temp > -40:
        return "⚠️ ALARM: High Moisture detected! Bypass to Standby Dryer."
    return "✅ System Dry."

# Example: 10k Liter tank at 40% with 250LPM demand
print(f"O2 Remaining: {oxygen_reserve_hours(10000, 40, 250)} Hours")
