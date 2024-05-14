from agents.information_gatherer.information_gatherer import InformationGatherer
from agents.data_verifier.data_verifier import DataVerifier
from agents.contract_drafter.contract_drafter import ContractDrafter
from agents.opposition_reviewer.opposition_reviewer import OppositionReviewer

def main_workflow(query):
    info_gatherer = InformationGatherer()
    data_verifier = DataVerifier()
    contract_drafter = ContractDrafter()
    opposition_reviewer = OppositionReviewer()

    try:
        # Gather information
        raw_data = info_gatherer.fetch_data(query)
        parsed_data = info_gatherer.parse_data(raw_data)

        # Verify data
        verified_data = data_verifier.verify_data(parsed_data)
        if not verified_data:
            raise ValueError("Data verification failed")

        # Draft contract
        draft = contract_drafter.draft_contract(verified_data)
        if not draft:
            raise ValueError("Failed to draft contract")

        # Review opposition
        review = opposition_reviewer.analyze_opposition(draft)
        return draft, review
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    result = main_workflow("Example Query")
    print(result)