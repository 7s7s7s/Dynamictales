story_data = {
    "introduction": {
        "scene": "Alex's Home Settlement",
        "event": "Discovery of the Communication Device"
    },
    "encounter_with_vega": {
        "scene": "Meeting Vega",
        "choice": {
            "trust_vega": "journey_through_wastelands",
            "continue_alone": "journey_through_wastelands"
        }
    },
    "journey_through_wastelands": {
        "scene": "First Tower Activation",
        "event": "Hostile Machine Encounter",
        "choice": {
            "fight": "ancient_ruins",
            "flee": "ancient_ruins",
            "negotiate": "ancient_ruins"
        }
    },
    "ancient_ruins": {
        "scene": "Puzzle Solving",
        "choice": {
            "success": "oracle_guidance",
            "failure": "oracle_guidance"
        }
    },
    "oracle_guidance": {
        "scene": "Oracle's Cryptic Message",
        "choice": {
            "trust": "final_tower",
            "question": "final_tower",
            "ignore": "final_tower"
        }
    },
    "final_tower": {
        "scene": "Final Tower Activation",
        "choice": {
            "restore_network": "conclusion",
            "reject_network": "conclusion",
            "partially_restore": "conclusion"
        }
    },
    "conclusion": {
        "outcome": {
            "restore_network": "Restoration of the Network",
            "reject_network": "Rejection of the Network",
            "partially_restore": "Compromise",
            "default": "The story has come to an end. What happens next is up to you."
        }
    }
}
